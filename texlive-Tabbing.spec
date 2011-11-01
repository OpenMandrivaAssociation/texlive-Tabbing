Name:		texlive-Tabbing
Version:	20100214
Release:	1
Summary:	Tabbing with accented letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//macros/latex/contrib/Tabbing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Tabbing.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
By default, some of the tabbing environment's commands clash
with default accent commands; LaTeX provides the odd commands
\a', etc., to deal with the clash. The package offers a variant
of the tabbing environment which does not create this
difficulty, so that users need not learn two sets of accent
commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
