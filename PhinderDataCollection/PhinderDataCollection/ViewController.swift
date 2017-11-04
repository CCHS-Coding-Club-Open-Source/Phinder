//
//  ViewController.swift
//  PhinderDataCollection
//
//  Created by Peter Maar on 11/4/17.
//  Copyright © 2017 alset333. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let hoursFromGMT = Double(TimeZone.current.secondsFromGMT()) / 3600.0
        
        print(TimeZone.current.abbreviation()!)
        
        let date = Date()
        let calendar = Calendar.current
        let hour = calendar.component(.hour, from: date)
        let minutes = calendar.component(.minute, from: date)
        
        
        print(hoursFromGMT)
        print(date, "\n", calendar, "\n", hour, "\n", minutes)
        
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

