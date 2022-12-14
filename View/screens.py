# Main screens
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController

from Model.setup_screen import SetupScreenModel
from Controller.setup_screen import SetupScreenController

# Admin screens
from Model.buttons_screen import ButtonsScreenModel
from Controller.buttons_screen import ButtonsScreenController

from Model.manage_users_screen import ManageUsersScreenModel
from Controller.manage_users_screen import ManageUsersScreenController

from Model.manage_route_screen import ManageRouteScreenModel
from Controller.manage_route_screen import ManageRouteScreenController

from Model.manage_checkpoint_screen import ManageCheckpointScreenModel
from Controller.manage_checkpoint_screen import ManageCheckpointScreenController

# Users screens
from Model.choose_route_screen import ChooseRouteScreenModel
from Controller.choose_route_screen import ChooseRouteScreenController

from Model.checkup_act_screen import CheckupActionScreenModel
from Controller.checkup_act_screen import CheckupActionScreenController


main_screen = {
    # name screen
    "login screen": {
        "model": LoginScreenModel,  # class of model
        "controller": LoginScreenController,  # class of controller
    },
    "setup screen": {
        "model": SetupScreenModel,  # class of model
        "controller": SetupScreenController,  # class of controller
    },
}

admin_screen = {
    "buttons screen": {
        "model": ButtonsScreenModel,  # class of model
        "controller": ButtonsScreenController,  # class of controller
    },
    "manage users screen": {
        "model": ManageUsersScreenModel,  # class of model
        "controller": ManageUsersScreenController,  # class of controller
    },
    "manage route screen": {
        "model": ManageRouteScreenModel,  # class of model
        "controller": ManageRouteScreenController,  # class of controller
    },
    "manage checkpoint screen": {
        "model": ManageCheckpointScreenModel,  # class of model
        "controller": ManageCheckpointScreenController,  # class of controller
    },
}

user_screen = {
    "choose route screen": {
        "model": ChooseRouteScreenModel,  # class of model
        "controller": ChooseRouteScreenController,  # class of controller
    },
    "checkup action screen": {
        "model": CheckupActionScreenModel,  # class of model
        "controller": CheckupActionScreenController,  # class of controller
    },
}
