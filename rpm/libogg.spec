Name:       libogg
Summary:    The Ogg bitstream file format library
Version:    1.3.3
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.xiph.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.



%package devel
Summary:    Files needed for development using libogg
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.


%package doc
Summary:    Documentation for the Ogg runtime library
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for developing applications with libogg



%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

chmod -x doc/*.html
rm -rf __installed_docs
mv $RPM_BUILD_ROOT%{_docdir}/%{name} __installed_docs


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING
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
%doc __installed_docs/*
