package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Profile struct {
	Name    string
	Hobbies []string
}

func main() {
	http.HandleFunc("/", foo)
	http.HandleFunc("/bar", bar)
	http.ListenAndServe(":9001", nil)
}

func foo(w http.ResponseWriter, r *http.Request) {
	// send request headers
	fmt.Fprintf(w, "%s %s %s\n", r.Method, r.URL, r.Proto)
	for key, value := range r.Header {
		fmt.Fprintf(w, "Header [%q] = %q\n", key, value)
	}
	fmt.Fprintf(w, "Host = %q\n", r.Host)
	fmt.Fprintf(w, "RemoteAddr = %q\n", r.RemoteAddr)
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}
	// send response headers
	w.Header().Set("Server", "A Go Web Server")
	w.WriteHeader(200)
}

func bar(w http.ResponseWriter, r *http.Request) {
	profile := Profile{"blah", []string{"foo", "bar"}}

	js, err := json.Marshal(profile)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(js)
}
