%define major 0
%define oname fakekey
%define libname %mklibname %{oname} %{major}
%define devname %mklibname -d %{oname}

Summary:		Converting characters to X key-presses
Name:			libfakekey
Version:		0.1
Release:		7
Group:			System/Libraries
License:		LGPLv2+
URL:			http://projects.o-hand.com/matchbox/
Source0:		http://matchbox-project.org/sources/libfakekey/0.1/%{name}-%{version}.tar.bz2
BuildRequires:		pkgconfig(xtst)
BuildRequires:		pkgconfig(x11)
BuildRequires:		pkgconfig(xi)

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{libname}
Summary:		Converting characters to X key-presses
Group:			System/Libraries

%description -n %{libname}
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{devname}
Summary:		Development files for %{name}
Group:			Development/C
Requires:		%{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export LDFLAGS="-lX11 -lXtst -lXi"
%configure \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfakekey.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc

