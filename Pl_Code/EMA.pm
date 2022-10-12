package EMA;
use strict;

sub new {
    my($proto, $length) = @_;
    die("$length: length must be a positive 32-bit integer")
        unless $length =~ /^\d+$/ && $length >= 1 && $length <= 0x7fff_ffff;
    return bless({
        alpha => 2 / ($length + 1),
    }, ref($proto) || $proto);
}

sub compute {
    my($self, $value) = @_;
    return $self->{avg} = defined($self->{avg})
        ? $value * $self->{alpha} + $self->{avg} * (1 - $self->{alpha})
        : $value;
}
1;