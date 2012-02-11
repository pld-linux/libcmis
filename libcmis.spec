Summary:	A C++ client library for the CMIS interface
Name:		libcmis
Version:	0.1.0
Release:	1
License:	GPL+ or LGPLv2+ or MPLv1.1
Group:		Libraries
URL:		http://sourceforge.net/projects/libcmis/
Source0:	http://downloads.sourceforge.net/libcmis/%{name}-%{version}.tar.gz
# Source0-md5:	4be634617054ada5b6d1886f63160f4f
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel

%description
LibCMIS is a C++ client library for the CMIS interface. This allows
C++ applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Command line tool to access CMIS
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

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

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.* README
%attr(755,root,root) %{_libdir}/%{name}-0.2.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}-0.2.so
%{_pkgconfigdir}/%{name}-0.2.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmis-client
