#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define pnam	Animation
Summary:	Term::Animation - ASCII sprite animation framework
Summary(pl):	Term::Animation - szkielet do animacji duszków ASCII
Name:		perl-Term-Animation
Version:	1.0
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b57a309b6a42051532e809dca6922af1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a framework to produce sprite animations using
ASCII art. Each ASCII 'sprite' is given one or more frames, and placed
into the animation as an 'animation object'. An animation object can
have a callback routine that controls the position and frame of the
object.

%description -l pl
Ten modu³ dostarcza szkielet do tworzenia animacji duszków przy u¿yciu
ASCII artu. Ka¿dy "duszek" ASCII jest zadany jedn± lub wiêksz± liczb±
ramek i umieszczany w animacji jako "obiekt animacji". Obiekt animacji
mo¿e mieæ wywo³anie zwrotne steruj±ce po³o¿eniem i ramk± obiektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/Animation.pm
%{_mandir}/man3/*
