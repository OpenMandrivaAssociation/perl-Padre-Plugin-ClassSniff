%define upstream_name    Padre-Plugin-ClassSniff
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple Class::Sniff interface for Padre
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Sniff)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Padre)
BuildRequires: perl(Test::More)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Runs Class::Sniff on the first namespace of the current document and prints
the results to the Padre output window.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
xvfb-run %{__perl} Makefile.PL INSTALLDIRS=vendor
%{make}

%check
xvfb-run %{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


