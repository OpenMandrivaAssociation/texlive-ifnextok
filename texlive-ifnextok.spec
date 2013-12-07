# revision 23379
# category Package
# catalog-ctan /macros/latex/contrib/ifnextok
# catalog-date 2011-06-27 20:36:28 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-ifnextok
Version:	0.3
Release:	3
Summary:	Utility macro: peek ahead without ignoring spaces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifnextok
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 752694
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718700
- texlive-ifnextok
- texlive-ifnextok
- texlive-ifnextok
- texlive-ifnextok

