%define	module	Term-Gnuplot

Name:		perl-%{module}
Version:	0.90380905
Release:	10
Summary:	Lowlevel graphics using gnuplot drawing routines
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
Patch0:		Term-Gnuplot-0.90380905-string-format-fix.patch
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	svgalib-devel
BuildRequires:	gnuplot
Requires:	    gnuplot
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	freetype-devel
buildRequires:	gd-devel

%description
Lowlevel graphics using gnuplot drawing routines.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .str_fmt~

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
yes "" | %{__make} test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*
