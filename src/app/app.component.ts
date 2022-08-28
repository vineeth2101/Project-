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
	constructor(private http: HttpClient) { }
	ngOnInit() {
	console.log("trying to conncet...............")
	//		this.http.get("http://13.232.155.224:5000/").subscribe(data => {
		this.http.get("http://13.234.225.231:5000/").subscribe(data => {
	//	this.http.get("http://172.31.39.45:5000/").subscribe(data => {
			console.log("::::::::::::::::::::;",data)
   })
   }
   }
