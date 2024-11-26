import 'package:flutter/material.dart';

class Pallete {
  static const cardColor = Color.fromRGBO(30, 30, 30, 1);
  static const greenColor = Colors.green;
  static const subtitleText = Color(0xffa7a7a7);
  static const inactiveBottomBarItemColor = Color(0xffababab);

  static const Color backgroundColor = Color.fromRGBO(18, 18, 18, 1);
  static const Color gradient1 = Color.fromRGBO(187, 63, 221, 1);
  static const Color gradient2 = Color.fromRGBO(251, 109, 169, 1);
  static const Color gradient3 = Color.fromRGBO(255, 159, 124, 1);
  static const Color borderColor = Color.fromRGBO(52, 51, 67, 1);
  static const Color whiteColor = Colors.white;
  static const Color greyColor = Colors.grey;
  static const Color errorColor = Colors.redAccent;
  static const Color transparentColor = Colors.transparent;

  static const Color inactiveSeekColor = Colors.white38;
}

// the palete class has all static variables because this way ,
//we dont need to create an instance of the class to get acess to the color
// so we can acess the color by saying : Pallete.cardColor instead of doing Pallete().cardColor
