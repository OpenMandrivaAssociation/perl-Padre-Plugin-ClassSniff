%define upstream_name    Padre-Plugin-ClassSniff
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simple Class::Sniff interface for Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Sniff)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::More)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
Runs Class::Sniff on the first namespace of the current document and prints
the results to the Padre output window.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
xvfb-run perl Build.PL installdirs=vendor
./Build

%check
xvfb-run ./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 657813
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 622951
- new version

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 447138
- running in a virtual framebuffer
- import perl-Padre-Plugin-ClassSniff


* Mon Sep 21 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
