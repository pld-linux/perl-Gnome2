#
# Conditional build:
%bcond_with tests 	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2
Summary:	Perl interface to the 2.x series of the Gnome libraries
Summary(pl):	Perlowy interfejs do bibliotek GNOME 2.x
Name:		perl-%{pnam}
Version:	0.32
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	c284b22b53807ee628c5f2ce8fe273bd
Patch0:		perl-%{pnam}-build_fix.patch
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	perl-Glib >= 0.95
BuildRequires:	perl-Gtk2 >= 0.95
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a perl developer to use the GNOME 2
libraries.

%description -l pl
Modu³ Perla Gnome2 pozwala programistom perlowym na u¿ywanie bibliotek
¶rodowiska GNOME 2.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO README druid.pl
%{perl_vendorarch}/%{pnam}.pm
%attr(755,root,root) %{perl_vendorarch}/auto/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pnam}/*.bs
%{_mandir}/man3/*
