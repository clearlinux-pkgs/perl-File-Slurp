#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Slurp
Version  : 9999.22
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/File-Slurp-9999.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/File-Slurp-9999.22.tar.gz
Summary  : 'Simple and Efficient Reading/Writing/Modifying of Complete Files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
# NAME
File::Slurp - Simple and Efficient Reading/Writing/Modifying of Complete Files

%package dev
Summary: dev components for the perl-File-Slurp package.
Group: Development
Provides: perl-File-Slurp-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Slurp package.


%prep
%setup -q -n File-Slurp-9999.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/File/Slurp.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Slurp.3
