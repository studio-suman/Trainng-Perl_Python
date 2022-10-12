package Test;
use strict;

sub plan {
    my($args) = {@_};
    Carp::croak('should not be called more than once')
        if $_TODO;
    _reset_globals();
    _read_program((caller)[1]);
    _plan_print(_plan_args($args));
    return;
}

sub _plan_args {
    my($args) = @_;
    $_ONFAIL = _plan_arg_assert($args, ['onfail'], 'CODE');
    my($max) = _plan_arg_assert($args, ['tests', 'test'], 'integer') || 0;
    # $_TODO is the initialization sentinel, so it's the last value set
    $_TODO = {map {$_ => 1}
        @{_plan_arg_assert($args, ['todo', 'failok'], 'ARRAY') || []}};
    Carp::carp("@{[sort(keys(%$args))]}: skipping unrecognized or",
        ' deprecated directive(s)')
        if %$args;
    return $max;
}

sub _plan_arg_assert {
    my($args, $names, $type) = @_;
    foreach my $n (@$names) {
        next unless exists($args->{$n});
        Carp::croak("$n: parameter must not be undef")
            unless defined($args->{$n});
        Carp::croak("$args->{$n}: $n must be $type")
            unless $type eq 'integer' ? $args->{$n} =~ /^\d+$/
                : ref($args->{$n}) eq $type;
        return delete($args->{$n})
    }
    return undef;
}

sub _plan_print {
    my($max) = @_;
    _print(join("\n# ",
        "1..$max"
            . (%$_TODO ne '' && " todo @{[sort {$a <=> $b} keys(%$_TODO)]};"),
        "Running under perl version $] for $^O"
            . (chr(65) ne 'A' && ' in a non-ASCII world'),
        defined(&Win32::BuildNumber) && defined(Win32::BuildNumber())
            ? 'Win32::BuildNumber ' . Win32::BuildNumber() : (),
        defined($MacPerl::Version)
            ? "MacPerl version $MacPerl::Version" : (),
        'Current time local: ' . localtime($^T),
        'Current time GMT: ' . gmtime($^T),
        "Using Test.pm version $VERSION\n"));
    return;
}

sub _print {
    local($\, $,);
    return print($TESTOUT @_);
}