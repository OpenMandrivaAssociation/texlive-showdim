# revision 28918
# category Package
# catalog-ctan /macros/latex/contrib/showdim/showdim.sty
# catalog-date 2012-12-19 17:06:30 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-showdim
Version:	1.2
Release:	4
Summary:	Variants on printing dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showdim/showdim.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showdim.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showdim.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for LaTeX providing a number of commands for printing
the value of a TeX dimension. For example,
\tenthpt{\baselineskip} yields the current value of
\baselineskip rounded to the nearest tenth of a point.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showdim/showdim.sty
%doc %{_texmfdistdir}/doc/latex/showdim/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
