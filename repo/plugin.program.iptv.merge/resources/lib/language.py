from matthuisman.language import BaseLanguage

class Language(BaseLanguage):
    SETTING_FETCH_EVERY_X  = 30000
    SETTING_AUTO_RELOAD    = 30001
    SETTING_FILES_DIR      = 30002
    ADD_EPG                = 30003
    ADD_PLAYLIST           = 30004
    MERGE_NOW              = 30005
    DELETE_SOURCE          = 30006
    CONFIRM_DELETE_SOURCE  = 30007
    MERGE_STARTED          = 30008
    NO_OUTPUT_DIR          = 30009
    PLAYLISTS              = 30010
    EPGS                   = 30011
    CHOOSE                 = 30012
    REMOTE_PATH            = 30013
    LOCAL_PATH             = 30014
    URL                    = 30015
    BROWSE_FILE            = 30016
    STANDARD_FILE          = 30017
    GZIPPED_FILE           = 30018
    RESET_CHANNEL          = 30019
    AUTO_MERGE             = 30020
    MERGE_IN_PROGRESS      = 30021
    ADDON_METHOD_FAILED    = 30022
    NO_GZIP_BINARY         = 30023
    GZIP_FAILED            = 30024
    MERGE_COMPLETE         = 30025
    ADDON_SOURCE           = 30026
    NO_ADDONS              = 30027
    SETUP_IPTV_SIMPLE      = 30028
    NO_IPTV_SIMPLE         = 30029
    SETUP_COMPLETE         = 30030
    LOCAL_PATH_MISSING     = 30031
    PLAY                   = 30032
    CHANNEL_MANAGER        = 30033
    NO_CHANNELS            = 30034
    NO_CHANNELS_MSG        = 30035
    NO_CHANNEL_NAME        = 30036
    HIDDEN                 = 30037
    CHANNEL_WITH_NUMBER    = 30038
    SHOW_CHANNEL           = 30039
    HIDE_CHANNEL           = 30040
    RENAME_CHANNEL         = 30041
    SET_CHANNEL_NUMBER     = 30042
    SET_CHANNEL_LOGO       = 30043
    SET_CHANNEL_GROUP      = 30044
    TV                     = 30045
    RADIO                  = 30046
    CHANNEL_WITH_GROUP     = 30047
    ADDON_METHOD_TIMEOUT   = 30048
    IMPORT_FILE            = 30049
    IMPORT_EXPORT          = 30050
    EXPORT_FILE            = 30051
    SELECT_IMPORT_FILE     = 30052
    SELECT_EXPORT_FOLDER   = 30053
    SOURCES_IMPORTED       = 30054
    SOURCES_EXPORTED       = 30055
    NO_EPG                 = 30056
    DISABLED               = 30057
    MOVE_UP                = 30058
    MOVE_DOWN              = 30059
    DISABLE_SOURCE         = 30060
    ENABLE_SOURCE          = 30061
    EDIT_SOURCE            = 30062
    DELETE_CHANNEL         = 30063
    ADD_CHANNEL            = 30064
    CHANNEL_PATH           = 30065
    URL_TAKEN              = 30066
    SET_CHANNEL_ID         = 30067
    CURRENT_EPG            = 30068
    ASSIGNED_EPG           = 30069
    CUSTOM_EPG             = 30070
    BEST_MATCH_EPG         = 30071
    EPG_ID_LABEL           = 30072
    DEFAULT_HIDDEN         = 30073

_ = Language()