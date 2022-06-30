use chilkat();

$spider = chilkat::CkSpider->new();

$seenDomains = chilkat::CkStringArray->new();
$seedUrls = chilkat::CkStringArray->new();

$seenDomains->put_Unique(1);
$seedUrls->put_Unique(1);

#  You will need to change the start URL to something else...
$seedUrls->Append("http://google.com/");

#  Set outbound URL exclude patterns
#  URLs matching any of these patterns will not be added to the
#  collection of outbound links.
$spider->AddAvoidOutboundLinkPattern("*?id=*");
$spider->AddAvoidOutboundLinkPattern("*.mypages.*");
$spider->AddAvoidOutboundLinkPattern("*.personal.*");
$spider->AddAvoidOutboundLinkPattern("*.comcast.*");
$spider->AddAvoidOutboundLinkPattern("*.aol.*");
$spider->AddAvoidOutboundLinkPattern("*~*");

#  Use a cache so we don't have to re-fetch URLs previously fetched.
$spider->put_CacheDir("c:/spiderCache/");
$spider->put_FetchFromCache(1);
$spider->put_UpdateCache(1);

while ($seedUrls->get_Count() > 0) {

    $url = $seedUrls->pop();
    $spider->Initialize($url);

    #  Spider 5 URLs of this domain.
    #  but first, save the base domain in seenDomains
    $domain = $spider->getUrlDomain($url);
    $seenDomains->Append($spider->getBaseDomain($domain));

    for ($i = 0; $i <= 4; $i++) {
        $success = $spider->CrawlNext();
        if ($success == 1) {

            #  Display the URL we just crawled.
            print $spider->lastUrl() . "\r\n";

            #  If the last URL was retrieved from cache,
            #  we won't wait.  Otherwise we'll wait 1 second
            #  before fetching the next URL.
            if ($spider->get_LastFromCache() != 1) {
                $spider->SleepMs(1000);
            }

        }
        else {
            #  cause the loop to exit..
            $i = 999;
        }

    }

    #  Add the outbound links to seedUrls, except
    #  for the domains we've already seen.
    for ($i = 0; $i <= $spider->get_NumOutboundLinks() - 1; $i++) {

        $url = $spider->getOutboundLink($i);
        $domain = $spider->getUrlDomain($url);
        $baseDomain = $spider->getBaseDomain($domain);
        if ($seenDomains->Contains($baseDomain) == 0) {
            #  Don't let our list of seedUrls grow too large.
            if ($seedUrls->get_Count() < 1000) {
                $seedUrls->Append($url);
            }

        }

    }

}