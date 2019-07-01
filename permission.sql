/*
Navicat MySQL Data Transfer

Source Server         : phpstudy
Source Server Version : 80012
Source Host           : localhost:3307
Source Database       : adam

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2019-07-01 16:03:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `ID` int(11) NOT NULL,
  `PermissionName` varchar(32) NOT NULL,
  `Description` varchar(128) NOT NULL,
  `Url` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES ('1', '所有权限', '最高管理员所有', '/admin');

-- ----------------------------
-- Table structure for pertorole
-- ----------------------------
DROP TABLE IF EXISTS `pertorole`;
CREATE TABLE `pertorole` (
  `ID` int(11) NOT NULL,
  `RoleId` int(11) NOT NULL,
  `PerId` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pertorole
-- ----------------------------
INSERT INTO `pertorole` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `ID` int(11) NOT NULL,
  `RoleName` varchar(32) NOT NULL,
  `Description` varchar(128) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('1', 'Admin', '最高权限管理员');
INSERT INTO `role` VALUES ('2', 'Guest', '普通管理员');

-- ----------------------------
-- Table structure for roletouser
-- ----------------------------
DROP TABLE IF EXISTS `roletouser`;
CREATE TABLE `roletouser` (
  `ID` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `RoleId` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roletouser
-- ----------------------------
INSERT INTO `roletouser` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `ID` int(11) NOT NULL,
  `UserName` varchar(32) NOT NULL,
  `RealName` varchar(32) NOT NULL,
  `PassWord` varchar(32) NOT NULL,
  `PhoneNumber` varchar(11) NOT NULL,
  `CreateTime` datetime(6) NOT NULL,
  `LastLogin` datetime(6) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'Adam', 'adam', 'adam', '12345678111', '2019-06-26 11:41:21.000000', '2019-07-01 10:39:59.883221');
INSERT INTO `userinfo` VALUES ('2', 'Test', 'test', 'test', '1234', '2019-06-26 16:48:15.000000', '2019-07-01 10:42:02.012893');
