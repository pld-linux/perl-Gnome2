#
# Conditional build:
%bcond_with	tests 	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gnome2
Summary:	Perl interface to the 2.x series of the GNOME libraries
Summary(pl):	Interfejs perlowy do bibliotek GNOME 2.x
Name:		perl-Gnome2
Version:	1.040
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	0a2dbefaafc5884cbeaf88968ebfe3ad
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.14.1
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.120
BuildRequires:	perl-Gnome2-Canvas >= 1.002
BuildRequires:	perl-Gnome2-VFS >= 1.060
BuildRequires:	perl-Gtk2 >= 1.121
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.120
Requires:	perl-Gnome2-Canvas >= 1.002
Requires:	perl-Gnome2-VFS >= 1.060
Requires:	perl-Gtk2 >= 1.121
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a Perl developer to use the GNOME 2
libraries.

%description -l pl
Modu³ Perla Gnome2 pozwala programistom perlowym na u¿ywanie bibliotek
¶rodowiska GNOME 2.

%prep
%setup -q -n %{pdir}-%{version}

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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/%{pdir}/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{perl_vendorarch}/%{pdir}/Install
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{perl_vendorarch}/auto/%{pdir}/*.bs
%{perl_vendorarch}/%{pdir}/Install/*
%{perl_vendorarch}/%{pdir}.pm
%{_mandir}/man3/*
