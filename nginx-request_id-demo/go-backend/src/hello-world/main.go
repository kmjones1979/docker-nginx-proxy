package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

var logf *os.File
var loggerINFO *log.Logger

type Profile struct {
	Name    string
	Hobbies []string
}

func init() {
	// log init
	logf, err := os.OpenFile("/var/log/go/go_access.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		fmt.Printf("ERROR: %v", err)
		os.Exit(1)
	}
	loggerINFO = log.New(logf, "INFO: ", log.Lshortfile|log.LstdFlags)
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
		fmt.Fprintf(w, "%v: %v\n", key, strings.Join(value, ","))
	}
	fmt.Fprintf(w, "Host: %v\nRemoteAddr:%v", r.Host, r.RemoteAddr)
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}

	// send response headers
	w.Header().Set("Server", "A Go Web Server")
	w.WriteHeader(200)

	// log details of the request
	loggerINFO.Println(r.Method, r.URL, r.Proto, r.Header, "Host: "+r.Host, "RemoteAddr"+r.RemoteAddr)
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
