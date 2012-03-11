Summary:	A C++ client library for the CMIS interface
Summary(pl.UTF-8):     Biblioteka klienta C++ dla inferfejsu CMIS
Name:		libcmis
Version:	0.1.0
Release:	2
License:	GPL+ or LGPLv2+ or MPLv1.1
Group:		Libraries
URL:		http://sourceforge.net/projects/libcmis/
Source0:	http://downloads.sourceforge.net/libcmis/%{name}-%{version}.tar.gz
# Source0-md5:	4be634617054ada5b6d1886f63160f4f
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibCMIS is a C++ client library for the CMIS interface. This allows
C++ applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%description -l pl.UTF-8
LibCMIS to biblioteka klienta C++  dla interfejsu CMIS. Pozwala ona 
aplikacjom C++ do łączenia się z każdym ECM zachowującym sie jako CMIS
serwer jak Alfresco, Nuxeo dla otwarto źródłowych aplikacji

%package devel
Summary:	Development files for %{name}
Summary(pl.UTF-8):	Pliki nagłówkowe dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description devel -l pl.UTF-8
Paczka %{name}-devel zawiera biblioteki i pliki nagłówkowe do
tworzenia aplikacji opartych na %{name}.

%package tools
Summary:	Command line tool to access CMIS
Summary(pl.UTF-8):	Narzędzie wiersza poleceń dla CMIS
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

%description tools -l pl.UTF-8
Paczka %{name}-tools zawiera narzędzie do łączenia się do CMIS
z wiersza poleceń.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-tests \
	--disable-werror

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/%{name}-0.2.so.*.*.*
%ghost %{_libdir}/libcmis-0.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-0.2.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}-0.2.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmis-client
