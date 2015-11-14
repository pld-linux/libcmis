#
# Conditonal build:
%bcond_without	static_libs	# static library
#
Summary:	A C++ client library for the CMIS interface
Summary(pl.UTF-8):     Biblioteka klienta C++ dla inferfejsu CMIS
Name:		libcmis
Version:	0.5.0
Release:	7
License:	GPL v2+ or LGPL v2+ or MPL v1.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcmis/%{name}-%{version}.tar.gz
# Source0-md5:	5821b806a98e6c38370970e682ce76e8
Patch0:		%{name}-boost-gcc.patch
URL:		http://sourceforge.net/projects/libcmis/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	cppunit-devel >= 1.12
BuildRequires:	curl-devel >= 7.12.3
BuildRequires:	docbook2X >= 0.8.8-4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	curl-libs >= 7.12.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibCMIS is a C++ client library for the CMIS interface. This allows
C++ applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%description -l pl.UTF-8
LibCMIS to biblioteka klienta C++ dla interfejsu CMIS. Pozwala ona 
aplikacjom C++ na łączenie się z każdym ECM zachowującym się jako
serwer CMIS, taki jak Alfresco, Nuxeo (biorąc pod uwagę implementacje
o otwartych źródłach).

%package devel
Summary:	Development files for CMIS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CMIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel
Requires:	curl-devel >= 7.12.3
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0

%description devel
This package contains the header files for developing applications
that use CMIS library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
bibliotece CMIS

%package static
Summary:	Static CMIS library
Summary(pl.UTF-8):	Statyczna biblioteka CMIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CMIS library.

%description static -l pl.UTF-8
Statyczna biblioteka CMIS.

%package tools
Summary:	Command line tool to access CMIS
Summary(pl.UTF-8):	Narzędzie wiersza poleceń dla CMIS
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains a tool for accessing CMIS from the command line.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzie do łączenia się do CMIS z wiersza
poleceń.

%prep
%setup -q
%patch0 -p1

#%{__sed} -i -e 's/docbook-to-man/docbook2X2man/' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	DOCBOOK2MAN=/usr/bin/docbook2X2man \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-tests \
	--disable-werror

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcmis-0.5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmis-0.5.so.5
%attr(755,root,root) %{_libdir}/libcmis-c-0.5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmis-c-0.5.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmis-0.5.so
%attr(755,root,root) %{_libdir}/libcmis-c-0.5.so
%{_includedir}/libcmis-0.5
%{_includedir}/libcmis-c-0.5
%{_pkgconfigdir}/libcmis-0.5.pc
%{_pkgconfigdir}/libcmis-c-0.5.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcmis-0.5.a
%{_libdir}/libcmis-c-0.5.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmis-client
%{_mandir}/man1/cmis-client.1*
