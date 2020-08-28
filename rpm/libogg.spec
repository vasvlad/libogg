Name:       libogg
Summary:    The Ogg bitstream file format library
Version:    1.3.4
Release:    1
License:    BSD
URL:        https://www.xiph.org/
Source0:    %{name}-%{version}.tar.bz2
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


%package doc
Summary:    Documentation for the Ogg runtime library
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for developing applications with libogg


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-static
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libogg.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS CHANGES README.md
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
