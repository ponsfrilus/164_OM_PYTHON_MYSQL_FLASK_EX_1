"""Définition des erreurs personnalisées
    Auteur : OM 2022.03.22 Utilisé lors de l'envoi de messages Flash avec le microframework FLASK
"""
class Grave(Exception):
    """
    Définit en cas d'erreur grave (exemple : sys.exit() si une variable d'environnement n'est pas définie)
    un message particulier.
    Affiche avec FLash l'erreur sur la page HTML
    """

    def __init__(self, message):
        self.message = message


class Base(Exception):
    """
    Définit en cas d'erreur presque normale (exemple : )
    un message particulier.
    Affiche avec FLash l'erreur sur la page HTML
    """

    def __init__(self, message):
        self.message = message


# --


class ServerInternalError(Grave):
    pass


class AuthentificationException(Base):
    pass


class DatabaseException(Base):
    pass


# --


class AppException(ServerInternalError):
    pass


class InitialisationException(ServerInternalError):
    pass


class DatabaseConnectionException(DatabaseException):
    pass


class SqlException(DatabaseException):
    pass


class EmptyPassword(AuthentificationException):
    pass


class PermissionsDenied(AuthentificationException):
    pass


# --


class FileException(AppException):
    pass


class EndpointBuildException(AppException):
    pass


class HTMLException(AppException):
    pass


class SqlSyntaxError(SqlException):
    pass


class IntegrityConstraintException(SqlException):
    pass


class WrongDataType(SqlException):
    pass


# --


class DumpFileException(FileException):
    pass


class EnvFileException(FileException):
    pass


class ExtractDatabaseNameException(FileException):
    pass


class DatabaseConnectionFailed(DatabaseConnectionException):
    pass


# --


class EnvVariablesException(EnvFileException):
    pass


class SqlCommandMissing(DumpFileException):
    pass


class DumpFileMissing(DumpFileException):
    pass


class ErreurFichierSqlDump(Exception):
    """Erreur qui doit être affichée lorsque le fichier DUMP à un problème"""
    pass


class ErreurConnectionBD(Exception):
    """Erreur qui doit être affichée lorsque la connection à la bd pose un problème"""
    pass