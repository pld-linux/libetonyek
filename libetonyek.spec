#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library and tools for reading and converting Apple Keynote presentations
Summary(pl.UTF-8):	Biblioteka i narzędzia do odczytu i konwersji prezentacji Apple Keynote
Name:		libetonyek
Version:	0.0.3
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	6deb26eb088acd8938b9bec800cfb59e
URL:		http://www.freedesktop.org/wiki/Software/libetonyek/
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libetonyek is a library and a set of tools for reading and converting
Apple Keynote presentations. The library tries to extract the most
important parts of version 2 format of Keynote (version 1 is not
supported yet, but it should be in the future). See FEATURES for what
is currently supported.

%description -l pl.UTF-8
libetonyek to biblioteka i zestaw narzędzi do odczytu i konwersji
prezentacji Apple Keynote. Biblioteka próbuje wydobyć najważniejsze
części formatu Keynote w wersji 2 (wersja 1 nie jest jeszcze
obsługiwana, ale powinna być w przyszłości). Informacje o
obsługiwanych elementach można znaleźć w pliku FEATURES.

%package devel
Summary:	Header files for libetonyek library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libetonyek
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9

%description devel
Header files for libetonyek library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libetonyek.

%package static
Summary:	Static libetonyek library
Summary(pl.UTF-8):	Statyczna biblioteka libetonyek
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libetonyek library.

%description static -l pl.UTF-8
Statyczna biblioteka libetonyek.

%package apidocs
Summary:	libetonyek API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libetonyek
Group:		Documentation

%description apidocs
API documentation for libetonyek library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libetonyek.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--disable-werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libetonyek-*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libetonyek

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FEATURES NEWS README TODO
%attr(755,root,root) %{_bindir}/key2raw
%attr(755,root,root) %{_bindir}/key2text
%attr(755,root,root) %{_bindir}/key2xhtml
%attr(755,root,root) %{_libdir}/libetonyek-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetonyek-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetonyek-0.0.so
%{_includedir}/libetonyek-0.0
%{_pkgconfigdir}/libetonyek-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libetonyek-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
