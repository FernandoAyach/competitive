#include <iostream>
#include <unordered_map>
#include <sstream>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();

    for (int w = 0; w < n; w++) {
        int d, m;
        std::cin >> d >> m;
        std::cin.ignore();

        std::unordered_map<std::string, std::string> translate;

        for (int i = 0; i < d; i++) {
            std::string japanese, portuguese;
            std::getline(std::cin, japanese);
            std::getline(std::cin, portuguese);
            translate[japanese] = portuguese;
        }

        for (int i = 0; i < m; i++) {
            std::string lyrics;
            std::getline(std::cin, lyrics);

            std::istringstream iss(lyrics);
            bool first = true;

            std::string word;
            while (iss >> word) {
                if (first)
                    first = false;
                else
                    std::cout << ' ';

                auto it = translate.find(word);
                if (it != translate.end()) {
                    std::cout << it->second;
                } else {
                    std::cout << word;
                }
            }

            std::cout << '\n';
        }
        std::cout << '\n';
    }

    return 0;
}
