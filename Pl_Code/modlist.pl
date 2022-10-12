use strict;

# Abe's "V" module can be found at
#	http://www.test-smoke.org/otherperl.html
# Module::CoreList is on CPAN, or fetch the most recent from
#	http://public.activestate.com/pub/apc/perl-current/lib/Module/CoreList.pm
#	just drop it into your actual location of something like
#	/usr/lib/perl5/site_perl/5.8.8/Module/
# If you're a pour soul that happens to use a perl without defined-or,
#	you will have to scan this file for // and replace it with the
#	appropriate core sections (all 6 occurances).

our $VERSION = 0.11;

BEGIN { $V::NO_EXIT = 1 }
require V;

use warnings;

sub usage ($;@)
{
    my $err = shift and select STDERR;
    print "usage: $0 [ -a AUT ] [ -r ] [ -i ] [ -nc ] [ <pattern> ]\n",
	"	-a | --author=AUTHOR_ID  Only modules from author\n",
	"	-r | --registered        Only registered modules\n",
	"	-i | --installed         Only installed modules\n",
	"	-n | --new               Only new modules\n",
	"	-c | --csv               Output module and version as CSV\n",
	"	<pattern>                Only modules that match pattern\n";
    exit $err;
    } # usage

@ARGV == 1 and $ARGV[0] eq "-?" || $ARGV[0] =~ m/^-+help$/ and usage (0);

use Text::CSV_XS;
use CPAN::Config;
use IO::Zlib;
use Module::CoreList;
use Getopt::Long qw(:config bundling nopermute);
my $author	= "";
my $registered	= 0;	# Default ALL modules
my $no_colors	= 0;
my $installed	= 0;
my $new		= 0;
my $skip_core	= 0;	# Skip "Core since ..."
my $csv;
GetOptions (
    "a|author|userid=s"	=> \$author,
    "r|registered"	=> \$registered,
    "i|installed"	=> \$installed,
    "n|new"		=> \$new,
    "no-core"		=> \$skip_core,
    "nc|no-colors"	=> \$no_colors,
    "c|csv"		=> \$csv,
    ) or usage (1);

my $pattern = shift // ".";

if ($csv) {
    $csv = Text::CSV_XS->new ({ binary => 1, auto_diag => 1, eol => "\n" });
    $no_colors++;
    }

if ($no_colors) {
    sub color { ""; }
    }
else {
    eval "use Term::ANSIColor";
    }

# *REGISTERED* packages in 03modlist
{   my $modlist = $CPAN::Config->{keep_source_where}."/modules/03modlist.data.gz";
    my $fh = IO::Zlib->new ($modlist, "rb") or die "Cannot open $modlist: $!\n";

    # Setting $/ to "\n\n" to skip the header got broken between 5.9.5 and 5.10

    # $/ broken for IO::Zlib
    (my $mlm = join "", <$fh>) =~ s{^.*\n\n}{}s;

    # Read the module-list structures
    eval $mlm;
    }
my %ml = %{CPAN::Modulelist::data ()};

# *ALL* packages in 02packages
{   my $details = $CPAN::Config->{keep_source_where}."/modules/02packages.details.txt.gz";
    my $fh = IO::Zlib->new ($details, "rb") or die "Cannot open $details: $!\n";

    # Skip the header
    {   local $/ = "\n\n";
	scalar <$fh>;
	}

    # Read the module-list structures
    while (<$fh>) {
	my ($m, $vsn, $tgz) = m{^(\S+)\s+(\S+)\s+(\S+)} or next;
	# Skip entries for the header record (names, name, fetch and mldistwatch)
	my ($userid, $distro) = ($tgz =~ m{^./../([^/]+)/(.*)}) or next;
	$distro =~s{\.t(ar\.)?gz$}{};
	#printf STDERR "%14s\t%-30s %8s\t%s\n", $userid, $m, $vsn, $distro; 
	$ml{$m} = {
	    userid	=> $userid,
	    description	=> "",
	    } unless exists $ml{$m};
	$ml{$m}{vsn} = $vsn;
	$ml{$m}{pkg} = $distro;
	}
    }

my %cl;
unless ($skip_core) {
    foreach my $pv (sort keys %Module::CoreList::version) {
	foreach my $m (keys %{$Module::CoreList::version{$pv}}) {
	    $cl{$m} //= $pv;
	    }
	}
    }

binmode STDOUT, ":utf8";

my $cReset = color ("reset");
my ($nmod, $m, $desc, $vsn, @pvsn) = (0);
foreach $m (sort keys %ml) {
    $desc = $ml{$m}{description};
    $registered && $desc eq "" and next;
    if ($author) {
	$ml{$m}{userid} =~ m{$author}io or next;
	}
    else {
	"$m\n$desc" =~ m{$pattern}io or next;
	}
    unless ($nmod++) {
	my $hc = color ("bold yellow on_black");
	printf "%s%-25s%s %s%-44s%s %sVersion %s\n",
	    $hc, "Module name", $cReset, $hc, "Description", $cReset, $hc, $cReset;
	}
    local $~ = $desc ? length ($m) > 25 ? "MLONG" : "MSHORT" : "MNODSC";
    if (($vsn = V::get_version ($m) // "")) {
	$new       and next;
	$installed or  print color ("white on_red");
	}
    else {
	$installed and next;
	}
    if ($csv) {
	$csv->print (*STDOUT, [ $m, $vsn ]);
	next;
	}
    $vsn //= $ml{$m}{vsn};
    write;
    if (exists $cl{$m}) {
	local $~ = "CLVSN";
	$pvsn[0] = $cl{$m};
	$pvsn[1] = $Module::CoreList::version{$pvsn[0]}{$m} // "-";
	$pvsn[3] = $Module::CoreList::version{$pvsn[2] = $]}{$m} // "-";
	write;
	}
    }

format MNODSC =
@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< @>>>>>>>@*
$m, $vsn, $cReset
.
format MSHORT =
@<<<<<<<<<<<<<<<<<<<<<<<< @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< @>>>>>>>@*
$m, $desc, $vsn, $cReset
.
format MLONG  =
@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
$m
                          @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< @>>>>>>>@*
$desc, $vsn, $cReset
.
format CLVSN =
                          Core since @>>>>>>> @>>>>>>      in @>>>>>>> @>>>>>>>
                          @pvsn
.