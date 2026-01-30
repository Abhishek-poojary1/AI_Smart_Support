import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://192.168.0.114:8001";

  // Upload PDF
  static Future<void> uploadPdf(File file) async {
    var request = http.MultipartRequest('POST', Uri.parse('$baseUrl/upload/'));

    request.files.add(await http.MultipartFile.fromPath('file', file.path));

    await request.send();
  }

  // Chat with AI
  static Future<Map<String, dynamic>> askQuestion(String query) async {
    final response = await http.post(
      Uri.parse('$baseUrl/chat/'),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"query": query}),
    );

    return jsonDecode(response.body);
  }
}
