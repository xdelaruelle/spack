# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RLog4r(RPackage):
    """logr4 provides an object-oriented logging system that uses an
    API roughly equivalent to log4j and its related variants."""

    homepage = "https://cran.r-project.org/package=log4r"
    url      = "https://cran.rstudio.com/src/contrib/log4r_0.2.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/log4r"

    version('0.2', 'f3fcb7b1f48526c6543b2e00e278ff65')

    depends_on('r-testthat', type=('build', 'run'))
