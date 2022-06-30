use feature qw(say);
use Net::LDAP

$ldap = Net::LDAP->new ("blr-ec-dc01.wipro.com");

my $user = "hsass";
my $mesg = $ldap->search(
    base => "blr-ec-dc01.wipro.com:636/DC=wipro,DC=com",
    filter => '(&(sAMAccountName=' . $user . ')(mail=*))',   #?!?
);
for my $entry ($mesg->entries) {
    my $val = $entry->get_value('mail');
    say "==$val==";
}