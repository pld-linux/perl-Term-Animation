#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Term
%define		pnam	Animation
%include	/usr/lib/rpm/macros.perl
Summary:	Term::Animation - ASCII sprite animation framework
Summary(pl.UTF-8):	Term::Animation - szkielet do animacji duszków ASCII
Name:		perl-Term-Animation
Version:	2.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d22643b339495cfc0a4f0b405dbae1d1
URL:		http://search.cpan.org/dist/Term-Animation/
BuildRequires:	perl-Curses >= 1.06
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

%description -l pl.UTF-8
Ten moduł dostarcza szkielet do tworzenia animacji duszków przy użyciu
ASCII artu. Każdy "duszek" ASCII jest zadany jedną lub większą liczbą
ramek i umieszczany w animacji jako "obiekt animacji". Obiekt animacji
może mieć wywołanie zwrotne sterujące położeniem i ramką obiektu.

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
%{perl_vendorlib}/Term/Animation
%{_mandir}/man3/*
