# revision 17022
# category Package
# catalog-ctan /macros/latex/contrib/Tabbing
# catalog-date 2010-02-14 11:55:47 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-Tabbing
Version:	20100214
Release:	4
Summary:	Tabbing with accented letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/Tabbing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
By default, some of the tabbing environment's commands clash
with default accent commands; LaTeX provides the odd commands
\a', etc., to deal with the clash. The package offers a variant
of the tabbing environment which does not create this
difficulty, so that users need not learn two sets of accent
commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/Tabbing/Tabbing.sty
%doc %{_texmfdistdir}/doc/latex/Tabbing/00readme
%doc %{_texmfdistdir}/doc/latex/Tabbing/Tabbing.pdf
#- source
%doc %{_texmfdistdir}/source/latex/Tabbing/Tabbing.dtx
%doc %{_texmfdistdir}/source/latex/Tabbing/Tabbing.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100214-2
+ Revision: 756426
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100214-1
+ Revision: 719632
- texlive-Tabbing
- texlive-Tabbing
- texlive-Tabbing
- texlive-Tabbing
- texlive-Tabbing

