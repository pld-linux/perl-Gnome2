#
# Conditional build:
%bcond_with tests 	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2
Summary:	Perl interface to the 2.x series of the Gnome libraries
Summary(pl):	Perlowy interfejs do bibliotek GNOME 2.x
Name:		perl-%{pnam}
Version:	0.93
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	263d907c861e1dd9992dc3a62c19f2e3
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.035
BuildRequires:	perl-Gnome2-Canvas >= 0.92
BuildRequires:	perl-Gnome2-VFS >= 0.96
BuildRequires:	perl-Gtk2 >= 1.021
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.035
Requires:	perl-Gnome2-Canvas >= 0.92
Requires:	perl-Gnome2-VFS >= 0.96
Requires:	perl-Gtk2 >= 1.021
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a perl developer to use the GNOME 2
libraries.

%description -l pl
Modu³ Perla Gnome2 pozwala programistom perlowym na u¿ywanie bibliotek
¶rodowiska GNOME 2.

%prep
%setup -q -n %{pnam}-%{version}

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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pnam}/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{perl_vendorarch}/%{pnam}/Install
%attr(755,root,root) %{perl_vendorarch}/auto/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pnam}/*.bs
%{perl_vendorarch}/%{pnam}/Install/*
%{perl_vendorarch}/%{pnam}.pm
%{_mandir}/man3/*
