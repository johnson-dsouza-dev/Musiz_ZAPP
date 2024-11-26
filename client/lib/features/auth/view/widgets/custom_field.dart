import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  final String hinText;
  final bool isObsceureText;
  final TextEditingController controller;
  const CustomField(
      {super.key,
      required this.hinText,
      required this.controller,
      this.isObsceureText = false});
  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      validator: (val) {
        if (val!.trim().isEmpty) {
          return "$hinText is missing!";
        }
        return null;
      },
      obscureText: isObsceureText,
      decoration: InputDecoration(
        hintText: hinText,
      ),
    );
  }
}
