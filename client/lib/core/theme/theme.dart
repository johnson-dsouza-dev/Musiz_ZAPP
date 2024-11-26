import 'package:client/core/theme/app_pallete.dart';
import 'package:flutter/material.dart';

class AppTheme {
  static final darkThemeMode = ThemeData.dark().copyWith(
    scaffoldBackgroundColor: Pallete.backgroundColor,
// we use copyWith() to overide the default scaffold color in flutter with
//the color we want using  Pallete.background that we have set in app_pallete

    // stting input decoration through out the app
    inputDecorationTheme: InputDecorationTheme(
      contentPadding: EdgeInsets.all(28),
      enabledBorder: _border(Pallete.borderColor),
      focusedBorder: _border(Pallete.gradient2),
    ),
  );

  static OutlineInputBorder _border(Color color) {
    return OutlineInputBorder(
      borderRadius: BorderRadius.circular(10),
      borderSide: BorderSide(
        width: 3,
        color: color,
      ),
    );
  }
}
