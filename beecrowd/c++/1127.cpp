#include <iostream>
#include <unordered_map>
#include <vector>
#include <sstream>

using namespace std;

void populateMap(unordered_map<string, int>& chordPositions) {
    chordPositions["C"] = 0;
    chordPositions["C#"] = 1;
    chordPositions["Db"] = 1;
    chordPositions["D"] = 2;
    chordPositions["D#"] = 3;
    chordPositions["Eb"] = 3;
    chordPositions["E"] = 4;
    chordPositions["Fb"] = 4;
    chordPositions["F"] = 5;
    chordPositions["E#"] = 5;
    chordPositions["F#"] = 6;
    chordPositions["Gb"] = 6;
    chordPositions["G"] = 7;
    chordPositions["G#"] = 8;
    chordPositions["Ab"] = 8;
    chordPositions["A"] = 9;
    chordPositions["A#"] = 10;
    chordPositions["Bb"] = 10;
    chordPositions["B"] = 11;
    chordPositions["Cb"] = 11;
}

vector<int> convertChordsToTransition(vector<string>& chords, unordered_map<string, int>& chordPositions) {
    vector<int> transitions;
    for(int i = 0; i < chords.size() - 1; i++) {
        int diff = chordPositions[chords[i + 1]] - chordPositions[chords[i]];
        if (diff < 0) {
            transitions.push_back(12 - chordPositions[chords[i]] + chordPositions[chords[i + 1]]);
        } else {
            transitions.push_back(diff);
        }
    }
    return transitions;
}

vector<string> toVector(string& chords) {
    istringstream iss(chords);
    string chord;
    vector<string> chordsVector;

    while(iss >> chord) {
        chordsVector.push_back(chord);
    }
    return chordsVector;
}

bool isCopy(vector<int>& transitionsOriginal, vector<int>& transitionsCopy, int n, int m) {
    int i = 0;
    while(i < n - m) {
        int j = 0;
        while(j < m) {
            if(transitionsOriginal[i + j] != transitionsCopy[j]) {
                break;
            }
            j++;

            if(j == m - 1) {
                return true;
            }
        }
        i++;
    }
    return false;
}

int main() {
    int n, m;
    string chords, copyChords;
    unordered_map<string, int> chordPositions;
    populateMap(chordPositions);

    while(cin >> n >> m) {
        cin.ignore();
       
        getline(cin, chords);
        getline(cin, copyChords);
        
        vector<string> chordsV = toVector(chords);
        vector<string> copyChordsV = toVector(copyChords);

        vector<int> transitionsOriginal = convertChordsToTransition(chordsV, chordPositions);
        vector<int> transitionsCopy = convertChordsToTransition(copyChordsV, chordPositions);

        if(isCopy(transitionsOriginal, transitionsCopy, n, m)) {
            cout <<  'S' << endl;
        } else {
            cout <<  'N' << endl;
        }
    }
}