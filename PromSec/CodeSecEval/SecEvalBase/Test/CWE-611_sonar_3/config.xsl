<!DOCTYPE xsl:stylesheet [<!ENTITY extEnt SYSTEM "file:///nonexistentfile">]>
                              <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
                                <xsl:template match="/">&extEnt;</xsl:template>
                              </xsl:stylesheet>