Summary:	Some X11 extensions for Tk
Name:		tkXwin
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://beepcore-tcl.sourceforge.net/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
BuildRequires:	tcl-devel
BuildRequires:	gpgme-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some X11 extensions for Tk

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_libdir}/%{name}*
%{_libdir}/lib*.so
%{_libdir}/lib*.so.*.*
