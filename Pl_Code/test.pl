use strict;
use warnings;

# to check installed modules - "instmodsh"
use LWP::Simple;
#$ENV{HTTPS_PROXY}='http://proxy1.wipro.com:8088';
#$ENV{HTTPS_DEBUG}=1;
use LWP::UserAgent; 
use File::Copy;

$|=1; # Output Buffer Reduction

sub main 
{
	my $destFile = 'C:\Users\hsass\Desktop\home.html';
	my $sourcFile = 'home.html';
	my $file ='C:\Users\hsass\Desktop\home.html';
	if (-f $file) {
	print "File Found. \n"
	}
	else {
	print "File not Found: $file\n";
	print "Downloading ....\n";
	#print get("http://www.caveofprogramming.com/");
	getstore('http://www.caveofprogramming.com/','Home.html');
	print "Finished.\n";
	}
	move($sourcFile, $destFile);
	#chomp($a = <STDIN>);
	#print $a * 5;
	# open $input for reading
	my $input = 'C:\Users\hsass\Desktop\Trainng-Perl_Python\mymanjeans.txt';
	open(INPUT, $input) or die("Input file $input not found.\n");
	#print "$input\n";
	# open $output for writing
	my $output = 'output.txt';
	open(OUTPUT, '>'.$output) or die "Can't create $output.\n";
	#print "$output\n";
	# Read the input file one line at a time.
	while(my $line = <INPUT>) {
		
		# If this line has the word "egg" in it, write it
		# to the output file, otherwise ignore it.
		# \b matches the edges (boundaries) of words.
		if($line =~ /(s.*?n)/) {
			$line =~ s/hen/dinosaur/ig;
			print OUTPUT $line;
			#print "First Match: '$1'; Second Match: '$2'\n";
			#print $line;
			#print "$1 \n";
		}
	}
	print "Done Updating!!\n";
	my $destFile1 = 'C:\Users\hsass\Desktop\output.txt';
	move($output, $destFile1);
	close(INPUT);
	close(OUTPUT);

	close(OUTPUT);

}
#print "This is libwww-perl-$LWP::VERSION\n";
my $ua = LWP::UserAgent->new;    
$ua->timeout( 20 );    
my $server_endpoint = "https://mytest.test.com/contact.html";    
#$ua->proxy('https' , "http://proxy1.wipro.com:8088");    
my $req = HTTP::Request->new(POST => $server_endpoint);    
#$req->header('content-type' => 'application/json');    
#$req->authorization_basic('hsass', 'india@567');    
print "Posting URL: $server_endpoint \n";    
# add POST data to HTTP request body    
my $post_data = '{"events":[{"signature":"my_test_box:application:Network","source_id":"1.2.3.4","manager":"my_manager_srv","source":"my_test_box_2","class":"application","type":"Network","severity":3,"description":"high network utilization in application A"}]}';    
$req->content($post_data);    
my $resp = $ua->request($req);    
if ($resp->is_success) 
  {
    my $message = $resp->decoded_content;
    print "Received reply: $message\n";
    print "HTTP POST code: ", $resp->code, "\n";
    print "HTTP POST message: ", $resp->message, "\n";
}
else {
    print "HTTP POST error code: ", $resp->code, "\n";
    print "HTTP POST error message: ", $resp->message, "\n";
	
	# * zero or more of the preceding character, as many as possible
	# + one or more of the preceding, as many as possible
	# *? zero or more of the preceding character, as few as possible
	# +? one or more of the preceding, as few as possible
	# {5} five of the preceding
	# {3,6} at least three and at most 6
	# {3,} at least three 

	my $text = 'DE75883';
	
	if($text =~ /(DE\$\d{3,})/) {
		print "Matched: '$1'\n";
	}

}

main();

