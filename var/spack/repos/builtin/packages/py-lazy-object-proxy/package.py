# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLazyObjectProxy(PythonPackage):
    """A fast and thorough lazy object proxy."""

    homepage = "https://github.com/ionelmc/python-lazy-object-proxy"
    url      = "https://pypi.io/packages/source/l/lazy-object-proxy/lazy-object-proxy-1.3.1.tar.gz"

    version('1.3.1', sha256='eb91be369f945f10d3a49f5f9be8b3d0b93a4c2be8f8a5b83b0571b8123e0a7a')

    conflicts('^python@3.0:3.2.99')

    depends_on('py-setuptools', type='build')
