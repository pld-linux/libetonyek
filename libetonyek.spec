#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Library and tools for reading and converting Apple Keynote presentations
Summary(pl.UTF-8):	Biblioteka i narzędzia do odczytu i konwersji prezentacji Apple Keynote
Name:		libetonyek
Version:	0.1.12
Release:	2
License:	MPL v2.0
Group:		Libraries
Source0:	https://dev-www.libreoffice.org/src/libetonyek/%{name}-%{version}.tar.xz
# Source0-md5:	e06865dc05f8de18e3dde991d65157c3
URL:		https://wiki.documentfoundation.org/DLP/Libraries/libetonyek
BuildRequires:	GLM-devel
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf
BuildRequires:	liblangtag-devel
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mdds-devel >= 2.1
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	rpm-build >= 4.6
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
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel >= 6:4.7
Requires:	libxml2-devel >= 2.0
Requires:	zlib-devel

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
BuildArch:	noarch

%description apidocs
API documentation for libetonyek library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libetonyek.

%package tools
Summary:	Tools to transform Apple Keynote presentations into other formats
Summary(pl.UTF-8):	Programy przekształcania prezentacji Apple Keynote do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Apple Keynote presentations into other formats.
Currently supported: XHTML, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania prezentacji Apple Keynote do innych
formatów. Aktualnie obsługiwane są XHTML i format surowy.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

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
%doc AUTHORS ChangeLog FEATURES.md NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libetonyek-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetonyek-0.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetonyek-0.1.so
%{_includedir}/libetonyek-0.1
%{_pkgconfigdir}/libetonyek-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libetonyek-0.1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/key2raw
%attr(755,root,root) %{_bindir}/key2text
%attr(755,root,root) %{_bindir}/key2xhtml
%attr(755,root,root) %{_bindir}/numbers2csv
%attr(755,root,root) %{_bindir}/numbers2raw
%attr(755,root,root) %{_bindir}/numbers2text
%attr(755,root,root) %{_bindir}/pages2html
%attr(755,root,root) %{_bindir}/pages2raw
%attr(755,root,root) %{_bindir}/pages2text
