# Maintainer: Votre Nom <cs7778503@github.com>
pkgname=idor-map
pkgver=1.0.0
pkgrel=1
pkgdesc="Tool for detecting Insecure Direct Object References (IDOR) in web applications."
arch=('any')
url="https://github.com/0625963141-cyber/idor-map"
license=('MIT')
depends=('python')

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/0625963141-cyber/idor-map/archive/${pkgver}.tar.gz")

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    python setup.py install --root="${pkgdir}/" --optimize=1
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    python setup.py install --root="${pkgdir}/" --optimize=1
}
