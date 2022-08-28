import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
title = 'first';
totalAngularPackages:any;
	constructor(private http: HttpClient,) { }
	ngOnInit() {
	var routeUrl = window.location.href
	console.log("rrrrrrrroute",window.location.href)
	var url = routeUrl.slice(0,-5)
	console.log(":::::::::url",url)
	
	console.log("trying to conncet...............")
		this.http.get("http://13.232.124.37:5000/read").subscribe(data => {
			console.log("::::::::::::::::::::;",data)
   })
   }
   }
