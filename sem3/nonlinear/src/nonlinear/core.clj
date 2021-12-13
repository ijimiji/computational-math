(ns nonlinear.core
  (:gen-class))

(require '[oz.core :as oz])

(def pow 
  "A wrapper for Java pow function from Math."
  #(Math/pow %1 %2))

(def abs
  "A wrapper for Java abs function from Math."
  #(Math/abs %))

(def eps (pow 10 -7))

(def log 
  "Calculate logarithm with a base of e."
  #(Math/log %))

(defn dichotomy [f a b n]
  "Find interval [a, b] with dichotomy."
  (let [c (/ (+ a b) 2)
        diff (- b a)]
    (println n a (f a) b (f b) diff)
    (if (> diff (* 2 0.1))
      (let [[a b] (if (< (* (f a) (f c)) 0) [a c] [c b])]
        (dihotomy f a b (inc n)))
      [a b])))

(defn mpi [f x n]
  (let [y (f x)
        diff (abs (- x y))]
    (println n x y diff)
    (if (> diff eps)
      (mpi f y (inc n)) 
      y)))

(defn newton [f x n]
  (let [y (- x (f x))
        diff (abs (- x y))]
    (println n x y diff)
    (if (> diff eps)
      (newton f y (inc n)) 
      y)))

(defn f [x]
  "A given function f."
  (- (pow 2 x) (+ (pow x 2) 0.5)))

(defn create-plot [f a b]
  (oz/view! {:data {:values 
                    (for [x (range a b (pow 10 -1))] {:x x :y (f x) })}
             :width 300
             :height 300
             :encoding {:x {:field "x" 
                            :type "quantitative"
                            :scale "x"}
                        :y {:field "y" 
                            :type "quantitative"
                            :scale "y"}}
             :mark {:type "line" :interpolate "monotone"}}))


(dichotomy f -100 100 0)

(oz/start-server!)
(create-plot f -2 2)

(mpi 
  #(+ % (* -1/2 (- (pow 2 %) (pow % 2) 1/2)))
  -1 0)

(newton 
  #(/ (- (pow 2 %) (pow % 2) 1/2)
      (- (* (pow 2 -2/3) (log 2)) (* 2 -2/3)))
  -1 0)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))
