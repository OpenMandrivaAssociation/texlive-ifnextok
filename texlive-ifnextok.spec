# revision 23379
# category Package
# catalog-ctan /macros/latex/contrib/ifnextok
# catalog-date 2011-06-27 20:36:28 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-ifnextok
Version:	0.3
Release:	1
Summary:	Utility macro: peek ahead without ignoring spaces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifnextok
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package deals with the behaviour of the LaTeX internal
command \@ifnextchar, which skips blank spaces. This has the
potential to surprise users, since it can produce really
unwanted effects. A common example occurs with brackets
starting a line following \\: the command looks for an optional
argument, whereas the user wants the brackets to be printed.
The package offers commands and options for modifying this
behaviour, maybe limited to certain parts of the document
source.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifnextok/ifnextok.sty
%doc %{_texmfdistdir}/doc/latex/ifnextok/README
%doc %{_texmfdistdir}/doc/latex/ifnextok/RELEASEs.txt
%doc %{_texmfdistdir}/doc/latex/ifnextok/SRCFILEs.txt
%doc %{_texmfdistdir}/doc/latex/ifnextok/ifnextok.pdf
%doc %{_texmfdistdir}/doc/latex/ifnextok/testIfNT.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifnextok/ifnextok.tex
%doc %{_texmfdistdir}/source/latex/ifnextok/makedoc.cfg
%doc %{_texmfdistdir}/source/latex/ifnextok/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/ifnextok/testIfNT.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
