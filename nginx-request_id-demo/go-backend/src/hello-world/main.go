package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Profile struct {
	Name    string
	Hobbies []string
}

func main() {
	http.HandleFunc("/", foo)
	http.HandleFunc("/bar", bar)
	http.ListenAndServe(":7001", nil)
}

func foo(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Server", "A Go Web Server")
	w.WriteHeader(200)
	for key, value := range r.Header {
		fmt.Println(key+": ", value)
	}
}

func bar(w http.ResponseWriter, r *http.Request) {
	profile := Profile{"Kevin", []string{"art", "nerd"}}

	js, err := json.Marshal(profile)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(js)
}
