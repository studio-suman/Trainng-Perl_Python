use strict;
use warnings;
use LWP::UserAgent ();
use JSON;

$|=1; # Output Buffer Reduction
use Mojo;
 
 # sub main {
 # my $ua = LWP::UserAgent->new;

 # # my $response = $ua->get('http://www.perlmonks.org/?node_id=1193449');
 # my $response = $ua->get('http://google.com');

 # if ($response->is_success) {
		# my $output = 'output.txt';
		# open(OUTPUT,'>'.$output) or die "Can't create $output.\n";
        # #print $response->decoded_content;
		# my $temp = $response -> decoded_content;
		# #print OUTPUT $response -> decoded_content;
		# my $tojson   = to_json($response);
		# my $fromjson = from_json($temp);
		# print OUTPUT $fromjson;
 # }
 # else {
     # die $response->status_line;
	 
# close(OUTPUT);
 # }
 
 #webcrawler using Mojo
 
my $bot = Mojo->new;
 
$bot->on(res => sub {
    my ($bot, $scrape, $job, $res) = @_;
     
    $bot->enqueue($_) for $scrape->('#context');
});
 
$bot->enqueue('http://www.perlmonks.org/?node_id=1193449');
$bot->crawl;
$bot->init; 
$bot->say_start;
 # }
 # main();