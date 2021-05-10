#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pdir	Gnome2
Summary:	Perl interface to the 2.x series of the GNOME libraries
Summary(pl.UTF-8):	Interfejs perlowy do bibliotek GNOME 2.x
Name:		perl-Gnome2
Version:	1.047
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://download.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	7d52bcc96e5dcd3b2c9b7aa90937c157
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.14.1
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-devel >= 1.140
BuildRequires:	perl-Gnome2-Canvas-devel >= 1.002
BuildRequires:	perl-Gnome2-VFS-devel >= 1.060
BuildRequires:	perl-Gtk2-devel >= 1.140
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Number-Delta >= 1.0
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	libbonoboui >= 2.0.0
Requires:	libgnomeui >= 2.14.1
Requires:	perl-Glib >= 1.140
Requires:	perl-Gnome2-Canvas >= 1.002
Requires:	perl-Gnome2-VFS >= 1.060
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a Perl developer to use the GNOME 2
libraries.

%description -l pl.UTF-8
Moduł Perla Gnome2 pozwala programistom perlowym na używanie bibliotek
środowiska GNOME 2.

%package devel
Summary:	Development files for Perl Gnome2 bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2 dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	libbonoboui-devel >= 2.0.0
Requires:	libgnomeui-devel >= 2.14.1
Requires:	perl-Glib-devel >= 1.140
Requires:	perl-Gnome2-Canvas-devel >= 1.002
Requires:	perl-Gnome2-VFS-devel >= 1.060
Requires:	perl-Gtk2-devel >= 1.140

%description devel
Development files for Perl Gnome2 bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2 dla Perla.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{perl_vendorarch}/Gnome2.pm
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Gnome2.so
%{_mandir}/man3/Gnome2.3pm*
%{_mandir}/man3/Gnome2::*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Install
