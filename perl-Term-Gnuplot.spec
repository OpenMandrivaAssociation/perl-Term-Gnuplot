%define	module	Term-Gnuplot
%define	name	perl-%{module}
%define	version	0.90380905
%define	release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lowlevel graphics using gnuplot drawing routines
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	perl-devel
BuildRequires:	svgalib-devel
BuildRequires:	gnuplot
Requires:       gnuplot
BuildRequires:	libjpeg-devel
BuildRequires:	X11-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel

%description
Lowlevel graphics using gnuplot drawing routines.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
yes "" | %{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*


