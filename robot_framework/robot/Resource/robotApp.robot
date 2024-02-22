*** Settings ***
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/robot/Resource/PO/landing_robot.robot
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/robot/Resource/PO/TopNov.robot
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/robot/Resource/PO/Team.robot
*** Variables ***
*** Keywords ***
Go to landing page
    landing_robot.Navigate To
    landing_robot.verify page loaded

Go to "Team" page
    TopNov.select "Team" page
    Team.verify page loaded

validate "Team" page
    Team.verify page contents
