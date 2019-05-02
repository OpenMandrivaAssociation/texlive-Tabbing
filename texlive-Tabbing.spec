Name:		texlive-Tabbing
Version:	20190228
Release:	1
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
%{_texmfdistdir}/tex/latex/Tabbing
%doc %{_texmfdistdir}/doc/latex/Tabbing
#- source
%doc %{_texmfdistdir}/source/latex/Tabbing

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
