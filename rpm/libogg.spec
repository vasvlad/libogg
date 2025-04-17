%define keepstatic 1
Name:       libogg
Summary:    The Ogg bitstream file format library
Version:    1.3.5
Release:    1
License:    BSD
URL:        https://www.xiph.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.


%package devel
Summary:    Files needed for development using libogg
Requires:   %{name} = %{version}-%{release}

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.


%package devel-static
Summary:    Files needed for development using libogg

%description devel-static
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.


%package doc
Summary:    Documentation for the Ogg runtime library
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for developing applications with libogg


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
mkdir -p build
pushd build
cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
popd

%install
pushd build
%make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
#%{_libdir}/libogg.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS CHANGES README.md
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
#%{_libdir}/libogg.so
%{_libdir}/cmake/Ogg/*.cmake
%{_libdir}/pkgconfig/ogg.pc

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
